availability_choice = ((True, 'In stock'), (False, 'Out of stock'),)

email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
password_reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

size = ((1, 'XS'), (2, 'SM'), (3, 'M'), (4, 'L'), (5, 'XL'), (6, 'XXL'), (7, 'XXXL'),)

is_featured = ((False, "Not a featured."), (True, "Is featured."),)

order_status_choice = ((1, 'Pending'), (2, 'In Progress'), (3, 'Delivered'), (4, 'Cancelled'),)

soft_delete = ((True, "Soft Deleted"), (False, "Not Deleted"))

genesis_block = ((True, "Is a Genesis Block."), (False, "Is not a Genesis Block."),)

notice_status = ((True, "Send Notice Now"), (False, "Don't Send Notice Now"),)

importance_status = ((1, "Critical"), (2, "Very Important"), (3, "Important"))
STATUS = (('Active', 'Active'), ('Inactive', 'Inactive'),

)

USER_STATUS = (('Active', 'Active'), ('Waiting', 'Waiting for activation'), ('Inactive', 'Inactive'),)

VARIANTS = (('None', 'None'), ('Size', 'Size'), ('Color', 'Color'), ('Size-Color', 'Size-Color'),

)

OutStock = (('1', '2-3 Day'), ('2', 'In Stock'), ('3', 'Out Stock'), ('4', 'Pre-order'),)

AddressType = (('Home', 'Home'), ('Business', 'Business'),

)

PaymentSTATUS = (('True', 'Yes'), ('False', 'NO'),)
payment_status_choice = (
    ("Pending", "Pending"), ("Online Payment", "Online Payment"), ("Cash on Delivery", "Cash on Delivery"))
OrderStatus = (('New', 'New'), ('Accepted', 'Accepted'), ('Preparing', 'Preparing'), ('OnShipping', 'OnShipping'),
               ('Completed', 'Completed'), ('Canceled', 'Canceled'), ('Refund', 'Refund'),)

DeliveryBySystem = (('Ydoob', 'Ydoob'), ('Self', 'Self'),)

CommissionSystemType = (('Category', 'Category'), ('DigitalMarketing', 'Digital Marketing'), ('Referral', 'Referral'),
                        ('ShippingRate', 'Shipping Rate'),

)

SHIPPING_STATUS = (('Active', 'Active'), ('Inactive', 'Inactive'), ('Free', 'Free'),)

product_transaction_type = ((1, "BUY"), (2, "SELL"))
CASES_Finish = (('مستمرة', 'مستمرة'), ('مغلقة', 'مغلقة'), )
CASES_TYPE = (('مدني', 'مدني'), ('جنائي', 'جنائي'), ('أسرة', 'أسرة'), ('اداري', 'اداري'),)
Civil_TYPE = (('مدعي', 'مدعي'),
              ('مدعي عليه', 'مدعي عليه'),)


Family_CASES_TYPE = (('مدني ', 'مدني'), ('جنائي', 'جنائي'), ('أسرة', 'أسرة'), ('اداري', 'اداري'),),
Criminal_CASES_TYPE = (('مجني', 'مجني عليه'), ('متهم', 'متهم'), ),
