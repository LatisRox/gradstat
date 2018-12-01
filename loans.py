file_name =  "Student Loan Advisor Data v2.xlsx"
master_sheet =  "Master Sheet"
allowance_sheet = "State and Other Tax Allowance"
pell_sheet = "Pell Grant"
uni_major_sheet= "Uni-Major Master Sheet"
major_sheet="Major - ID (Reference)"
minimum_wage="Minimum Wage by State"
pell_grant="Pell Grant"


import pandas as pd
import numpy

#Load the Master Sheet
df = pd.read_excel(io=file_name, sheet_name=master_sheet)
#Load the State and Other Tax Allowance
df2 = pd.read_excel(io=file_name, sheet_name=allowance_sheet)
#Load the Uni-Major Master sheet
df3 = pd.read_excel(io=file_name, sheet_name=uni_major_sheet)
#Load the Major Sheet
df4 = pd.read_excel(io=file_name, sheet_name=major_sheet)
#Load the State sheet
df5 = pd.read_excel(io=file_name, sheet_name=minimum_wage)
#Load the Pell Grant Sheet
df6 = pd.read_excel(io=file_name, sheet_name=pell_grant)

#Return entry from the dataframe
def return_school_id(school_name) :
    return(df.loc[df["School Name"]==school_name]["School ID"].values[0]);
def return_school_info(school_id, info) :
    return(df.loc[df["School ID"]==school_id][info].values[0]);

#Return state and Tax total_Allowance
def return_tax(state, income) :
    if parent_income <= 15000:
        return(df2.loc[df2["State"]==state]["Income (0-14999)"].values[0]);
    else:
        return(df2.loc[df2["State"]==state]["Income (>15000)"].values[0]);


#Return state and Tax total_Allowance
def return_uni_major_pay(time) :
    major_id=df4.loc[df4["Major"]==major]["Suffix No."].values[0]
    return(df3.loc[(df3["School ID"]==university_id) & (df3["Major ID"]==major_id)][time].values[0]);

#Dynamic parameters to be changed according to the student's choices
parent_income=50000
university="Illinois State University"
live_with_parents=True
state_of_residence="Arkansas"
number_students=1
number_household=4
major="Business"

#numeric variables to be calculated
calculatedAttendanceCost=0
calculatedAllowance=0
calculatedStudentLoan=0
calculatedEarlyCareerPay=0
calculatedMidCareerPay=0
calculatedNPV=0
calculatedMonthlyPayment=0
calculatedMinimumWage=0
calculatedTotalPayment=0
#Find University ID
university_id=return_school_id(university)
#Find University State
university_state=return_school_info(university_id, "State")
minimum_wage_rate=df5.loc[df5["State"]==university_state]["Minimum Wage"].values[0]

print("Minimum Wage", minimum_wage_rate)
print("University of", university)

def do_all_calculations():

    #Calculate Cost of Attendance
    if university_state == state_of_residence :
        if live_with_parents == True :
            attendance_cost=return_school_info(university_id, "Total Cost of Attendance (In-State Living with Parents) per year")
        else:
            attendance_cost=return_school_info(university_id, "Total Cost of Attendance (In-State Living on-campus) per year")
    else :
        attendance_cost=return_school_info(university_id, "Total Cost of Attendance (Out-of-State Living on Campus) per year")
    global calculatedAttendanceCost
    calculatedAttendanceCost=attendance_cost
    print("Attendance Cost",attendance_cost)

    #Calculate US Income Tax Paid
    if parent_income <= 19050:
        income_tax = parent_income * 0.1
    elif parent_income <= 77400:
        income_tax = parent_income * 0.12
    elif parent_income <= 165000:
        income_tax = parent_income * 0.22
    elif parent_income <= 315000:
        income_tax = parent_income * 0.24
    elif parent_income <= 400000:
        income_tax = parent_income * 0.32
    elif parent_income <= 600000:
        income_tax = parent_income * 0.35
    else:
        income_tax = parent_income * 0.37

    #Calculate State and other Tax Allowance
    state_tax = parent_income*return_tax(state_of_residence, parent_income)

    #Calculate Employment Expense Allowance
    if parent_income <= 22857:
        employment_tax =  parent_income*0.35
    else:
        employment_tax = 4000;

    #Calculate Social Security Tax Allowance
    if parent_income <= 188501:
        socialSecurity_tax =  parent_income*0.0735
    else:
        socialSecurity_tax = 9065.25+0.0145*(parent_income-118500)

    #Calculate Income Protection Allowance
    incomeProtection_tax = 18320+4390*(number_household-2)-3120*(number_students-1)

    #Total Allowance
    total_Allowance=income_tax+state_tax+employment_tax+socialSecurity_tax+incomeProtection_tax
    global calculatedAllowance
    calculatedAllowance=total_Allowance
    print ("Allowance" ,total_Allowance)

    #Calculate Available income
    if parent_income >= total_Allowance:
        available_income=parent_income-total_Allowance
    else:
        available_income=0

    #Calculate Parent's contribution
    if available_income/number_students > attendance_cost :
        efc = attendance_cost
    else:
        efc = available_income/number_students

    print ("Expected Family Contribution", efc)


    #Calculate Financial Need
    if attendance_cost >= efc:
        financial_need = attendance_cost - efc
    else:
        financial_need = 0

    #Calculate Additional Grants
    federal_grants=0
    percent_federal_grants=return_school_info(university_id, "Percent Receiving Federal Grants")
    if (percent_federal_grants > 6.384E-17*parent_income**3-4.583651832E-11*parent_income**2+0.000011460936436527*parent_income-0.0572232769260302):
        federal_grants=return_school_info(university_id, "Average Amount of Federal Grant")

    print ("Federal Grants",federal_grants)

    state_grants=0
    percent_state_grants=return_school_info(university_id, "Percent Receiving State/Local Grants")
    if (percent_state_grants > 6.384E-17*parent_income**3-4.583651832E-11*parent_income**2+0.000011460936436527*parent_income-0.0572232769260302):
        state_grants=return_school_info(university_id, "Average Amount of Federal Grant")

    print ("State Grants",state_grants)

    institutional_grants=0
    percent_institutional_grants=return_school_info(university_id, "Percent Receiving Institutional Grants")
    if (percent_state_grants > 6.384E-17*parent_income**3-4.583651832E-11*parent_income**2+0.000011460936436527*parent_income-0.0572232769260302):
        institutional_grants=return_school_info(university_id, "Average Amount of Institutional Grant")

    print ("Percent Receiving Institutional Grants",institutional_grants)

    #Calculate Pell Grant
    if efc==0:
        row=0
    elif efc>56000:
        row=56
    else:
        row=int(round(efc/1000+1,1))

    if (attendance_cost>=60950):
        col=60
    else:
        col=int(round(attendance_cost/1000-1,1))

    pell_grant_amount=df6.iloc[col][row]

    if (financial_need-(federal_grants+state_grants+institutional_grants)<=pell_grant_amount):
        pell_grant_amount=0

    print("Pell Grant:", pell_grant_amount)

    #Calculate Student Loans
    student_loan=0
    if (financial_need>federal_grants+state_grants+institutional_grants+pell_grant_amount):
        student_loan =financial_need-(federal_grants+state_grants+institutional_grants+pell_grant_amount)
    global calculatedStudentLoan
    calculatedStudentLoan=student_loan
    print ("Student Loan",student_loan)

    #Calculate Early Career pay
    early_pay=return_uni_major_pay("Early Career Pay Median salary for alumni with 0-5 years experience")
    global calculatedEarlyCareerPay
    calculatedEarlyCareerPay=early_pay   
    print("Early pay",early_pay)

    #Calculate Mid Career pay
    mid_pay=return_uni_major_pay("Mid-Career Pay Median salary for alumni with 10+ years experience")
    global calculatedMidCareerPay
    calculatedMidCareerPay=mid_pay   
    print("Mid pay",mid_pay)

    #Calculate NPV
    #Calculate Wage increase
    increase_wage=(mid_pay/early_pay)**(1/15)-1
    global calculatedWageIncrease
    calculatedWageIncrease=increase_wage
    print("Increase Wage",increase_wage)


    #For NPV Calculation
    number_working_days=261
    number_working_hours=8
    yearly_hours=number_working_days*number_working_hours
    yearly_minimum_wage=yearly_hours*minimum_wage_rate
    global calculatedMinimumWage
    calculatedMinimumWage=yearly_minimum_wage
    inflation_rate=0.027
    discount_rate=0.051

    degree_earning=[]
    minimum_wage=[yearly_minimum_wage]
    difference_earning=[-yearly_minimum_wage]
    NPV=[(-yearly_minimum_wage)/((1+discount_rate)**(1-0.5))]

    for i in range(0,35):
        if i < 4:
            degree_earning.append(0)
        elif i==4:
            degree_earning.append(early_pay)
        elif i < 20:
            degree_earning.append(degree_earning[i-1]*(1+increase_wage))
        else:
            degree_earning.append(degree_earning[i-1]*(1+increase_wage/2))

    for j in range(1,35):
        minimum_wage.append(minimum_wage[j-1]*(1+inflation_rate))
        difference_earning.append(degree_earning[j]-minimum_wage[j])
        NPV.append(difference_earning[j]/((1+discount_rate)**(j+1-0.5)))

    # print("Degree Earning", degree_earning)
    # print(len(degree_earning))
    # print("Minimum Wage", minimum_wage)
    # print(len(minimum_wage))
    # print("Difference earning", difference_earning)
    # print(len(difference_earning))
    print("NPV", NPV)
    global calculatedNPV
    calculatedNPV=sum(NPV)
    print("NPV", sum(NPV))

    #Calculation of Monthly repayment
    #For 15 years Loan
    monthly_interest_rate=(1+discount_rate)**(1/12)-1
    montly_repayment=numpy.pmt(monthly_interest_rate,180,-student_loan)

    global calculatedMonthlyPayment
    calculatedMonthlyPayment=montly_repayment
    print("Monthly repayment for 15 years per each year loan", montly_repayment)
    global calculatedTotalPayment
    calculatedTotalPayment=4*montly_repayment
    print("Total monthly repayment for 15 years for 4 years of school", 4*montly_repayment)

#do_all_calculations()