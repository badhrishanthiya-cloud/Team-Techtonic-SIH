from flask import Flask, url_for, redirect, render_template, request
from programs import app, db
from programs.forms import LostForm, FoundForm, QRForm, FeedbackForm
from programs.models import lost, found, feedback
import base64
from rapidfuzz import fuzz
from programs.forms import QRForm
import qrcode
import base64
from io import BytesIO
from flask import flash


def calculate_fuzzy_score(lost_desc: str, found_desc: str) -> float:
    if not lost_desc or not found_desc:
        return 0.0
    # Token Set Ratio handles word ordering differences and partial matches well
    score = fuzz.token_set_ratio(lost_desc, found_desc)
    return round(float(score), 1)


@app.route("/delete-item/<int:item_id>", methods=["POST"])
def delete_item(item_id):
    # Fetch item from database
    item_to_delete = found.query.get_or_404(item_id)

    # Remove item from SQLite database
    db.session.delete(item_to_delete)
    db.session.commit()

    # Maintain query context when redirecting back
    search_desc = request.args.get("search_desc", "")
    return redirect(url_for("item_page", search_desc=search_desc))


@app.route("/")
@app.route("/home", methods=["GET", "POST"])
def home_page():
    form_feedback = FeedbackForm()
    if form_feedback.validate_on_submit():
        # Store feedback in the database
        user_feedback = feedback(
            name=form_feedback.name.data, message=form_feedback.message.data
        )
        db.session.add(user_feedback)
        db.session.commit()

        # Display success message
        flash("Thank you for your feedback!", "success")

        # Redirect back to the home page (reappears smoothly)
        return redirect(url_for("home_page"))

    return render_template("home.html", form_feedback=form_feedback)


@app.route("/items")
def item_page():
    # 1. Grab description passed from lost.html via URL parameter
    user_lost_desc = request.args.get("search_desc", "").strip()

    data = found.query.all()
    scored_items = []

    for item in data:
        image_b64 = None
        if item.image:
            image_b64 = base64.b64encode(item.image).decode("utf-8")

        # 2. Compare user's lost description against found item description
        match_score = calculate_fuzzy_score(user_lost_desc, item.description)

        scored_items.append(
            {
                "id": item.id,
                "name": item.name,
                "loc": item.loc,
                "phone": item.phone,
                "description": item.description,
                "image": image_b64,
                "score": match_score,  # Similarity score in percentage
            }
        )

    # 3. Sort items: highest percentage match appears first
    scored_items.sort(key=lambda x: x["score"], reverse=True)

    return render_template("items.html", items=scored_items, query_desc=user_lost_desc)


@app.route("/lost", methods=["GET", "POST"])
def lost_page():
    form_lost = LostForm()
    if form_lost.validate_on_submit():
        user_created_lost = lost(
            name=form_lost.name.data,
            phone=form_lost.phone.data,
            hostel=form_lost.hostel.data,
            loc=form_lost.loc.data,
            description=form_lost.description.data,
        )
        db.session.add(user_created_lost)
        db.session.commit()

        # 4. Redirect to /items and pass the description through query params
        return redirect(url_for("item_page", search_desc=form_lost.description.data))

    return render_template("lost.html", form_lost=form_lost)


@app.route("/thankyou")
def confirmation_page():
    return render_template("confirmation.html")


@app.route("/found", methods=["GET", "POST"])
def found_page():
    form_found = FoundForm()
    if form_found.validate_on_submit():
        user_created_found = found(
            name=form_found.name.data,
            phone=form_found.phone.data,
            loc=form_found.loc.data,
            description=form_found.description.data,
            image=form_found.image.data.read(),
        )
        db.session.add(user_created_found)
        db.session.commit()
        return redirect(url_for("confirmation_page"))
    return render_template("found.html", form_found=form_found)


@app.route("/qrcode", methods=["GET", "POST"])
def qrcode_generation_page():
    if request.method == "POST":
        # Extract submitted values from form
        name = request.form.get("name")
        hostel = request.form.get("hostel")
        phone = request.form.get("phone")
        item_name = request.form.get("item_name")

        # Format information string encoded inside the QR code
        qr_data = (
            f"NITK LOST & FOUND TAG\nOwner: {name}\nHostel: {hostel}\nPhone: {phone}"
        )

        # Generate QR Code Image
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=2,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Save QR Image into memory buffer as PNG
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        # Encode image buffer to Base64 string for template rendering
        qr_b64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

        return render_template(
            "qr.html",
            generated=True,
            qr_b64=qr_b64,
            name=name,
            hostel=hostel,
            phone=phone,
            item_name=item_name,
            tag_id=phone[-4:] if phone else "1234",
        )

    # Initial GET request (render blank form)
    return render_template("qrcode.html", generated=False)


@app.route("/qr", methods=["GET", "POST"])
def qrcode_page():
    form = QRForm()
    if form.validate_on_submit():
        return redirect(url_for("qrcode_generation_page"))
    return render_template("qr.html", form=form)
