from flask import Flask,render_template,request
app = Flask(__name__)
applications = {'CI00196310':'Credit IVR','CI00308110':'Fraud IVR','CI00415499':'IVR GIFT CARD'}
@app.route('/entry')
def entry() -> 'html':
    return render_template('entry.html',the_title='Welcome to Appliation Search')

@app.route('/search',methods=['POST'])
def search() -> 'html':
    blossomId = request.form['id']
    print(blossomId)
    print(applications[blossomId])
    title = 'Here are your results'
    return render_template('results.html',the_id=blossomId,the_title=title,the_results=applications[blossomId])

app.run()
