
import unittest

from person import Person
from staff import Staff
from student import Student
from program import Program
from school import School


class TestPerson(unittest.TestCase):
    def test_person_01_constructor( self ):
        p = Person("Mark", "Min Gata 1")
        self.assertEqual( str(p), "Person[name=Mark,address=Min Gata 1]" )

    def test_person_02_get_name( self ):
        p = Person("Mark", "Min Gata 1")
        self.assertEqual( p.getName(), "Mark" )

    def test_person_03_get_address( self ):
        p = Person("Mark", "Min Gata 1")
        self.assertEqual( p.getAddress(), "Min Gata 1" )

    def test_person_04_set_address( self ):
        p = Person("Mark", "Min Gata 1")
        p.setAddress( "Annan Gata 2" )
        self.assertEqual( p.getAddress(), "Annan Gata 2" )


class TestStudent(unittest.TestCase):
    def test_student_01_constructor( self ):
        p = Student("Mark", "Min Gata 1", "IoT", 17, 50000)
        self.assertEqual( str(p), "Student[Person[name=Mark,address=Min Gata 1],program=IoT,year=17,fee=50000.00]" )

    def test_student_02_get_program( self ):
        p = Student("Mark", "Min Gata 1", "IoT", 17, 50000)
        self.assertEqual( p.getProgram(), "IoT" )

    def test_student_03_set_program( self ):
        p = Student("Mark", "Min Gata 1", "IoT", 17, 50000)
        p.setProgram( "3D Design" )
        self.assertEqual( p.getProgram(), "3D Design" )

    def test_student_04_get_year( self ):
        p = Student("Mark", "Min Gata 1", "IoT", 17, 50000)
        self.assertEqual( p.getYear(), 17 )

    def test_student_05_set_year( self ):
        p = Student("Mark", "Min Gata 1", "IoT", 17, 50000)
        p.setYear(16)
        self.assertEqual( p.getYear(), 16 )

    def test_student_06_get_fee( self ):
        p = Student("Mark", "Min Gata 1", "IoT", 17, 50000)
        self.assertEqual( p.getFee(), 50000 )

    def test_student_07_set_fee( self ):
        p = Student("Mark", "Min Gata 1", "IoT", 17, 50000)
        p.setFee( 125.66 )
        self.assertEqual( p.getFee(), 125.66 )




class TestStaff(unittest.TestCase):
    def test_staff_01_constructor( self ):
        p = Staff("Mark", "Min Gata 1", "Nackademin", 50)
        self.assertEqual( str(p), "Staff[Person[name=Mark,address=Min Gata 1],school=Nackademin,pay=50.00]" )

    def test_staff_02_get_school( self ):
        p = Staff("Mark", "Min Gata 1", "Nackademin", 50)
        self.assertEqual( p.getSchool(), "Nackademin" )

    def test_staff_03_set_school( self ):
        p = Staff("Mark", "Min Gata 1", "Nackademin", 50)
        p.setSchool( "Medieinstitutet" )
        self.assertEqual( p.getSchool(), "Medieinstitutet" )

    def test_staff_04_get_pay( self ):
        p = Staff("Mark", "Min Gata 1", "Nackademin", 50)
        self.assertEqual( p.getPay(), 50 )

    def test_staff_05_set_pay( self ):
        p = Staff("Mark", "Min Gata 1", "Nackademin", 50)
        p.setPay( 125.66 )
        self.assertEqual( p.getPay(), 125.66 )

 

class TestProfit(unittest.TestCase): #Tesf of profit. First is the som of pay and fee calculaled and then they are compared.
    def test_profit_01_sumOfFee( self ):
        Nackadmein=School("Nackademin")
        studentx=Student("john", "gatan 12", "iot",17, 5000)
        studenty=Student("peter", "gatan 2", "iot",17, 5000)
        Iot=Program("IoT")
        Iot.addStudent(studentx)
        Iot.addStudent(studenty)
        self.assertEqual( Iot.sumOfFee(), 10000 )

    def test_profit_02_sumOfPay( self ):
        Nackadmein=School("Nackademin")
        staff1=Staff("Mark", "Tomteboda 1", "Nackademin", 50 )
        staff2=Staff("Pike", "Tomteboda 3", "Nackademin", 50 )
        Nackadmein.addStaff(staff1)
        Nackadmein.addStaff(staff2)
        self.assertEqual( Nackadmein.sumOfPay(), 100 )

    def test_profit_03_isProfit( self ):

        Nackadmein=School("Nackademin")
        iot=Program("IoT")
        Nackadmein.addProgram(iot) 

        studentA=Student("john", "gatan 12", "iot",17, 50)
        studentB=Student("peter", "gatan 2", "iot",17, 50)
        studentC=Student("pjotr", "gatan 2", "iot",17, 50)
        iot.addStudent(studentA)
        iot.addStudent(studentB)
        iot.addStudent(studentC)

        staff1=Staff("Mark", "Tomteboda 1", "Nackademin", 50 )
        staff2=Staff("Pike", "Tomteboda 3", "Nackademin", 50 )
        Nackadmein.addStaff(staff1)
        Nackadmein.addStaff(staff2)

        self.assertEqual( Nackadmein.getProfit(Nackadmein.sumOfPay(), iot.sumOfFee()), True )

    def test_profit_04_notProfit( self ):

        Nackadmein=School("Nackademin")
        iot=Program("IoT")
        java=Program("Java")
        Nackadmein.addProgram(iot) 
        Nackadmein.addProgram(java) 

        studentx=Student("john", "gatan 12", "iot",17, 50)
        studenty=Student("peter", "gatan 2", "iot",17, 50)
        studentz=Student("peter", "gatan 2", "iot",17, 40)
        iot.addStudent(studentx)
        iot.addStudent(studenty)
        java.addStudent(studentz)

        staff1=Staff("Mark", "Tomteboda 1", "Nackademin", 50 )
        staff2=Staff("Pike", "Tomteboda 3", "Nackademin", 50 )
        staff3=Staff("Moa", "Tomteboda 1", "Nackademin", 50 )
        Nackadmein.addStaff(staff1)
        Nackadmein.addStaff(staff2)
        Nackadmein.addStaff(staff3)

        self.assertEqual( Nackadmein.getProfit(Nackadmein.sumOfPay(), Nackadmein.totalFee()), False )
        

if __name__ == '__main__':
    unittest.main(verbosity=2)
