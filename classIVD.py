#this program to calculate fluid requirement intraop
class IVDrip:
	def __init__ (self):
		self.patient_weight=0.0
		self.ongoing_loss = 0.0
		self.time_nbm = 0.0


	def fluidmaintainance421(self):
		fluid = 0.0
		if self.patient_weight > 20.0:
			fluid=60.0+(self.patient_weight-20.0)
		else:
			if self.patient_weight<=10.0:
				fluid=self.patient_weight*4.0
			else:
				fluid= 40.0 + ((self.patient_weight-10)*2)
				
		
		return fluid
    
	def deficit(self):
		fluid = self.fluidmaintainance421()
		d = fluid*self.time_nbm
		return d
	
	def ongoing(self):
		o = self.ongoing_loss*self.patient_weight
		return o
		
	def get_patient_data(self):
		print("\nweight : ", self.patient_weight, " kg", "\nongoing loss : ", self.ongoing_loss, " mls / H" , "\nNBM", self.time_nbm, " Hours\n")
		
	def input_patient_data(self):
		self.patient_weight =float(input("what is patient weight ? \n"))
		self.ongoing_loss = float(input("what is ongoing loss \n"))
		self.time_nbm = float(input("how lomg pt patient NBm\n"))
		
print("this program calculate fluid requirement intraoperatively \n\n\n")
	

apis = IVDrip()


apis.input_patient_data()

print("	first hour : ", apis.fluidmaintainance421()+ 0.5*apis.deficit()+ apis.ongoing()," mls/h", 
"\n	2nd hour : " , apis.fluidmaintainance421()+apis.ongoing()+0.25*apis.deficit(), 
"\n	3rd hour : ", apis.fluidmaintainance421()+0.25*apis.deficit()+apis.ongoing(),
"\n	4th hour : " , apis.fluidmaintainance421()+apis.ongoing())

