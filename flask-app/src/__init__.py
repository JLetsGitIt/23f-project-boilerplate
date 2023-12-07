# Some set up for the application 

from flask import Flask
from flaskext.mysql import MySQL
from flask import Blueprint

# create a MySQL object that we will use in other parts of the API
db = MySQL()

def create_app():
    app = Flask(__name__)
    
    # secret key that will be used for securely signing the session 
    # cookie and can be used for any other security related needs by 
    # extensions or your application
    app.config['SECRET_KEY'] = 'someCrazyS3cR3T!Key.!'

    # these are for the DB object to be able to connect to MySQL. 
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = open('/secrets/db_root_password.txt').readline().strip()
    app.config['MYSQL_DATABASE_HOST'] = 'db'
    app.config['MYSQL_DATABASE_PORT'] = 3306
    app.config['MYSQL_DATABASE_DB'] = 'toy_sellers'  # Change this to your DB name

    # Initialize the database object with the settings above. 
    db.init_app(app)
    
    # Add the default route
    # Can be accessed from a web browser
    # http://ip_address:port/
    # Example: localhost:8001
    @app.route("/")
    def welcome():
        return "<h1>Welcome to the 3200 boilerplate app</h1>"

    # Import the various Beluprint Objects
    from src.customers.customers import customers
    from src.products.products  import products
    from src.customization.customization  import customization
    from src.customer.customer import customer
    from src.feedback.feedback import feedback
    from src.gift_wrapping_service.gift_wrapping_services import gift_wrapping
    from src.toy.toy import toy
    from src.order.order import order
    from src.toy_manufacturer.toy_manufacturer import toy_manufacturer
    from src.toy_safety_information import toy_safety_information
    
    # Register the routes from each Blueprint with the app object
    # and give a url prefix to each
    toy_information = Blueprint('toy info', __name__)
    toy_information.register_blueprint(toy, url_prefix='/c')
    toy_information.register_blueprint(customization, url_prefix='/p')
    toy_information.register_blueprint(toy_safety_information, url_prefix = '/ts')
    app.register_blueprint(toy_information, url_prefix='/t')

    customerandmanufacturer = Blueprint('people', __name__)
    customerandmanufacturer.register_blueprint(customer, url_prefix = '/cust')
    customerandmanufacturer.register_blueprint(toy_manufacturer, url_prefix = '/man')
    app.register_blueprint(customerandmanufacturer, url_prefix = '/cm')
    

    order_information = Blueprint('order_info', __name___)
    order_information.register_blueprint(order, url_prefix = '/o')
    order_information.register_blueprint(gift_wrapping, url_prefix = '/gw')
    app.register_blueprint(order_information, url_prefix = '/oi')

    feedback = Blueprint('feedback', __name__)
    feedback.register_blueprint(feedback, url_prefix = '/f')
    app.register_blueprint(feedback, url_prefix = '/feed')

    
    # Don't forget to return the app object
    return app
