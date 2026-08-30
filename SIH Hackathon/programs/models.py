from programs import db


class lost(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.Integer(), nullable=False)
    hostel = db.Column(db.String(60), nullable=False)
    loc = db.Column(db.String(1024), nullable=True)
    description = db.Column(db.String(1024), nullable=False)


class found(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.Integer(), nullable=False)
    loc = db.Column(db.String(1024), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    image = db.Column(db.LargeBinary)


class feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)
    # Optional: add name or email if you want to identify submitters
    name = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"<Feedback {self.id}>"
