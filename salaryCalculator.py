"""
1/12/2023 Program: salaryCalculator.py
GUI-based app used to calculate an employee's salary in a provided amount of hours
NOTE: The file breezypythongui.py MUST be in the same directory as this file for the app to run correctly!
"""
from breezypythongui import EasyFrame
from tkinter.font import Font
# other imports can go here
class SalaryCalculator(EasyFrame):
	# definiton of the __init__() method which is out class constructor
	def __init__(self):
		# call the EasyFrame constructor method
		EasyFrame.__init__(self, title = "Salary Calculator", background = "sienna", resizable = False)
		self.addLabel(text = "Salary Calculator", row = 0, column = 0, columnspan = 2, background = "burlywood", foreground = "sienna", sticky = "NSEW", font = Font(family = "Arial Black", size = 24))
		self.addLabel(text = "Hourly Wage:", row = 1, column = 0, background = "burlywood", foreground = "sienna", sticky = "NSEW")
		self.hourlyWage = self.addFloatField(value = 0.0, row = 1, column = 1, precision = 2, sticky = "NSEW")
		self.addLabel(text = "# of Hours Worked:", row = 2, column = 0, background = "burlywood", foreground = "sienna", sticky = "NSEW")
		self.hoursWorked = self.addIntegerField(value = 0, row = 2, column = 1, sticky = "NSEW")
		self.addButton(text = "Compute", row = 3, column = 0, columnspan = 2, command = self.compute)
		self.addLabel(text = "The employee's salary is:", row = 4, column = 0, background = "burlywood", foreground = "sienna", sticky = "NSEW")
		self.salary = self.addFloatField(value = 0.0, row = 4, column = 1, precision = 2, state = "readonly")
	# definition of the compute() method, our event handler
	def compute(self):
		# input phase for the GUI
		wage = self.hourlyWage.getNumber()
		hours = self.hoursWorked.getNumber()
		# processing phase
		total = wage * hours
		# output phase
		self.salary.setNumber(total)
# definition of the main() method which will establish class objects
def main():
	# instantiates an object from the class into mainloop()
	SalaryCalculator().mainloop()
# global call to the main() method
main()