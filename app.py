





from flask import Flask, render_template

app = Flask(__name__)

# Define products
products = {
    "product_1": {"name": "Product A",
                  "price": 100,
                  "features":[  "Feature_1",
                               "Feature_2",
                               "Feature_3", 
                            ], 
                  
                 },
    "product_2": {"name": "Product B", 
                  "price": 200,
                  "features":[ " Feature_10",
                              "Feature_11",
                              "Feature_12", 
                             
                            ], 
                 },
    "product_3": {"name": "Product C", 
                  "price": 300,
                  "features": [  "Feature_20",
                                "Feature_21",
                                "Feature_22", 
                               
                             ], 
                  },
}


@app.route('/', methods=['GET', 'POST'])

def index():    
    return render_template('index.html', products=products)


if __name__ == '__main__':
    app.run(debug=True)
