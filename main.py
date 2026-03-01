# Take user input
hours = float(input("Enter study hours: "))
attendance = float(input("Enter attendance percentage: "))
previous = float(input("Enter previous score: "))
assignments = float(input("Enter number of assignments completed: "))

# Make prediction
prediction = model.predict([[hours, attendance, previous, assignments]])

print("Predicted Final Score:", prediction[0])