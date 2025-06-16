from flask_wtf import FlaskForm
from wtforms import DecimalField
from wtforms import StringField, FloatField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Regexp

class AddProductForm(FlaskForm):
    name = StringField(
        "Name",
        validators=[
            DataRequired(),
            Regexp(r'^[a-zA-Z ]+$', message="Name must contain only letters (A-Z or a-z).")
        ]
    )
    category = StringField(
        "Category",
        validators=[
            DataRequired(),
            Regexp(r'^[a-zA-Z ]+$', message="Category must contain only letters (A-Z or a-z).")
        ]
    )
    price = DecimalField(
        "Price",
        places=4,
        rounding=None,
        validators=[DataRequired(), NumberRange(min=0)]
    )
    quantity = IntegerField("Quantity", validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField("Add Product")
