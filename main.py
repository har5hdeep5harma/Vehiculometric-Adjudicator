from os import read
from flask import Flask, request, render_template
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from modelbuilding import logistic, dtree, randomforest, svc, knn

app = Flask(__name__)

#Reading Data from file
def readdata():
    colnames=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']
    df = pd.read_csv('data/car.data', names=colnames)
    return df

#Groupby with Status Column
def getdict(colname):
    df = readdata()
    return dict(df.groupby([colname])['class'].count())

#Label Encoding
def labelencoding(df):
    data = df.copy()
    getmappings = {}
    for col in data.columns:
        encoder = LabelEncoder() 
        data[col] = encoder.fit_transform(data[col])
        getmappings[col] = dict(zip(encoder.classes_, encoder.transform(encoder.classes_)))

    return getmappings, data


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    getmappings, data=labelencoding(readdata())
    
    if request.method == 'POST':
        # Get form data
        mydict=request.form
        buy= mydict['buy']
        maintain = mydict['maintain']
        doors = mydict['doors']
        person = mydict['person']
        luggage = mydict['luggage']
        safety = mydict['safety']
        algo= mydict['algo']
        
        value=mydict['feature']
        values=["Buying", "Maintainance", "Doors", "Persons", "Luggage", "Safety"]
        keys=['buying', 'maint', 'doors', 'person', 'lug_boot', 'safety', 'class']
        mapper= dict(zip(values, keys))
        
        value_column = mapper.get(value)

        if not value_column:
            return render_template('index.html', display=False, showtemplate=False, error="Invalid feature name")

        valuecount = getdict(value_column)

        
        #Selection of Algorithm
        algomapper= {
            'rf': randomforest(data),
            'dt': dtree(data),
            'svc': svc(data)}
        
        classmapper = {0: 'Accurate', 1: 'Good', 2: 'Unaccurate', 3: 'Very Good'}
        algorithm= algomapper[algo]
        accuracy, recall, precision, f1score, model = algorithm
        
        inputparam = [[
    getmappings['buying'][buy],
    getmappings['maint'][maintain],
    getmappings['doors'][doors],
    getmappings['persons'][person],
    getmappings['lug_boot'][luggage],
    getmappings['safety'][safety]
]]

        predict= model.predict(inputparam)
        predictedclass = classmapper[predict[0]]
        
        return render_template('index.html', predictedclass=predictedclass, display=True, accuracy=round(accuracy*100, 2), precision=precision, showtemplate=True, valuecount=valuecount, value=mapper[value], mapper=valuecount) 
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
