from flask import Flask,request,render_template,jsonify
import pickle
import numpy as np

model = pickle.load(open('titanic.pkl','rb'))

app= Flask(__name__)

@app.route('/')
def get_data():
	return render_template('/titanic/titanic_data.html')

@app.route('/get_titanic_data', methods=["POST"])
def get_titanic_data():	



	data = request.form['pclass']	

	if data=='pclass1':
		data=1
	elif data=='pclass2':
		data=2
	else:
		data=3

	m_sex = request.form['sex']
	
	if m_sex =='M':
		m_sex=0
	else:
		m_sex=1

	data2 = request.form['age']

	data3 = request.form['sibsp']
	if data3=='sibsp1':
		data3=0
	else:
		data3=1

	data4 = request.form['parch']

	if data4=='parch1':
		data4=0
	else:
		data4=1	
	data5 = request.form['Fare']
	
	data6 = request.form['embarked']
	if data6=='embarked1':
		data6=0
	else: 
		data6=1	

	final_data = np.array([[data,m_sex,data2,data3,data4,data5,data6]])
	print(final_data)

	prediction = model.predict(final_data)
	print(prediction)

	return render_template('/titanic/titanic_data_final.html',prediction=prediction[0])

if __name__=='__main__':
	app.run(debug=True)