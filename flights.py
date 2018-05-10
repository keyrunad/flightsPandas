# Author: Keyrun Adhikari
# Advanced Python Homework 3
# Data analyzed: July, 2017
# Major holiday: July 4, 2017, Independence day

import pandas as pd
import matplotlib.pyplot as plt

def ques0():
    # function to remove all flights that were cancelled and diverted
    flightsData = pd.read_csv('flights.csv') # read flights.csv file

    cleanData = flightsData.loc[(flightsData['CANCELLED'] != float(1)) & (flightsData['DIVERTED'] != float(1))] # removing all flights that were cancelled and diverted
    cleanData = cleanData.reset_index() # reset cleanData index
    return cleanData

def ques1(cleanData):
    # function to calculate and print top 5 airlines in terms of ontime departure percentage, ontime arrival percentage, average departure lateness, average arrival lateness
    carrGbCount = cleanData.groupby('CARRIER').size() # count of number of flights by each carrier group
    otDep = cleanData[cleanData['DEP_DELAY'] <= 0] # ontime departed flights data only
    otDepCount = otDep.groupby('CARRIER').size() # count of number of ontime departed flights by each carrier group
    otDepPer = otDepCount/carrGbCount * 100 # ontime percentage for each carrier
    print('\nTop 5 airlines in terms of ontime departure percentage:')
    print(otDepPer.sort_values(ascending = False)[:5])
    otArr = cleanData[cleanData['ARR_DELAY'] <= 0] # ontime arrived flights data only
    otArrCount = otArr.groupby('CARRIER').size() # count of number of ontime departed flights by each carrier group
    otArrPer = otArrCount/carrGbCount * 100 # ontime departure percentage for each carrier
    print('\nTop 5 airlines in terms of ontime arrival percentage:')
    print(otArrPer.sort_values(ascending = False)[:5])
    lateDep = cleanData[cleanData['DEP_DELAY'] > 0] # late departed flights data only
    lateDepAvg = lateDep.groupby('CARRIER')['DEP_DELAY'].mean() # average departure lateness of each carrier group
    print('\nTop 5 airlines in terms of average departure lateness:')
    print(lateDepAvg.sort_values(ascending = False)[:5])
    lateArr = cleanData[cleanData['ARR_DELAY'] > 0] # late arrived flights data only
    lateArrAvg = lateArr.groupby('CARRIER')['ARR_DELAY'].mean() # average arrival lateness of each carrier group
    print('\nTop 5 airlines in terms of average arrival lateness:')
    print(lateArrAvg.sort_values(ascending = False)[:5])


def ques2(cleanData):
    # function to calculate and print the relative percentages of flights that leave and arrive on time vs leave on time and arrive late vs leave late and arrive on time vs leave and arrive late
    totFlights = len(cleanData.index) # total number of flights in the time period
    otDepOtArr = len(cleanData[(cleanData['DEP_DELAY'] <= 0) & (cleanData['ARR_DELAY'] <= 0)].index) # count of ontime departed and ontime arrived flights
    otDeplateArr = len(cleanData[(cleanData['DEP_DELAY'] <= 0) & (cleanData['ARR_DELAY'] > 0)].index) # count of ontime departed and late arrived flights
    lateDepOtArr = len(cleanData[(cleanData['DEP_DELAY'] > 0) & (cleanData['ARR_DELAY'] <= 0)].index) # count of late departed and ontime arrived flights
    lateDepLateArr = len(cleanData[(cleanData['DEP_DELAY'] > 0) & (cleanData['ARR_DELAY'] > 0)].index) # count of late departed and late arrived flights
    print('\nRelative percentage of flights that leave and arrive on time:\n', otDepOtArr/totFlights*100)
    print('\nRelative percentage of flights that leave on time and arrive late:\n', otDeplateArr/totFlights*100)
    print('\nRelative percentage of flights that leave late and arrive on time:\n', lateDepOtArr/totFlights*100)
    print('\nRelative percentage of flights that leave and arrive late:\n', lateDepLateArr/totFlights*100)

def ques3(cleanData):
    # funtion to find of if the northeast have worse time performance than the rest of the country
    neStates = ['CT', 'ME', 'MA', 'NH', 'NJ', 'NY', 'PA', 'RI', 'VT', 'DE', 'MD'] # list of states in connecticut
    northEastFl = cleanData[cleanData['ORIGIN_STATE_ABR'].isin(neStates)] # flights departing from states in northeast
    avgNeFl = northEastFl[northEastFl['DEP_DELAY'] > 0]['DEP_DELAY'].mean() # average departure lateness of flights departing northeast states
    restFl = cleanData[~cleanData['ORIGIN_STATE_ABR'].isin(neStates)] # flights departing from states other than in northeast
    avgRestFl = restFl[restFl['DEP_DELAY'] > 0]['DEP_DELAY'].mean() # average departure lateness of flights departing states other than northeast states
    print('\nTime performance of the states in northeast based on average departure lateness:\n', avgNeFl)
    print('\nTime performance of the states in rest of the country based on average departure lateness:\n', avgRestFl)
    if avgNeFl > avgRestFl:
        print('\nYes, states in the northeast have worse time performance than the rest of the country based on average departure lateness.\n')
    elif avgNeFl < avgRestFl:
        print('\nNo, states in the northeast do not have worse time performance than the rest of the country based on average departure lateness.\n')
    elif avgNeFl == avgRestFl:
        print('\nNo, states in the northeast have same time performance than the rest of the country based on average departure lateness.\n')

def ques4(cleanData):
    # function to calculate and print top 5 airports in terms of ontime departure percentage, ontime arrival percentage, average departure lateness, average arrival lateness
    originGbCount = cleanData.groupby('ORIGIN').size() # count of number of flights by each origin airport group
    destGbCount = cleanData.groupby('DEST').size() # count of number of flights by each destination airport group
    otDep = cleanData[cleanData['DEP_DELAY'] <= 0] # ontime departed flights data only
    otDepCount = otDep.groupby('ORIGIN').size() # count of number of ontime departed flights by each airport group
    otDepPer = otDepCount/originGbCount * 100 # ontime percentage for each airport
    print('\nTop 5 airports in terms of ontime departure percentage:')
    print(otDepPer.sort_values(ascending = False)[:5])
    otArr = cleanData[cleanData['ARR_DELAY'] <= 0] # ontime arrived flights data only
    otArrCount = otArr.groupby('DEST').size() # count of number of ontime departed flights by each airport group
    otArrPer = otArrCount/destGbCount * 100 # ontime departure percentage for each airport
    print('\nTop 5 airports in terms of ontime arrival percentage:')
    print(otArrPer.sort_values(ascending = False)[:5])
    lateDep = cleanData[cleanData['DEP_DELAY'] > 0] # late departed flights data only
    lateDepAvg = lateDep.groupby('ORIGIN')['DEP_DELAY'].mean() # average of departure delay for each origin
    print('\nTop 5 airports in terms of average departure lateness:')
    print(lateDepAvg.sort_values(ascending = False)[:5])
    lateArr = cleanData[cleanData['ARR_DELAY'] > 0] # late arrived flights data only
    lateArrAvg = lateArr.groupby('DEST')['ARR_DELAY'].mean()
    print('\nTop 5 airports in terms of average arrival lateness:')
    print(lateArrAvg.sort_values(ascending = False)[:5])

def ques5(cleanData):
    # function to calculate and print the top 5 airlines in terms of the longest taxi out and taxi in times for each of five major airports
    majAirports = ['LAX', 'JFK', 'DFW', 'ORD', 'ATL']
    majApDepFl = cleanData[cleanData['ORIGIN'].isin(majAirports)]
    originGb = majApDepFl.groupby('ORIGIN')
    print('\nTop 5 airlines in terms of longest taxi out for five major airports:')
    print(originGb.apply(lambda origin: origin.groupby('CARRIER')['TAXI_OUT'].max().sort_values(ascending = False)[:5]))
    majApArrFl = cleanData[cleanData['DEST'].isin(majAirports)]
    destGb = majApArrFl.groupby('DEST')
    print('\nTop 5 airlines in terms of longest taxi in for five major airports:')
    print(destGb.apply(lambda dest: dest.groupby('CARRIER')['TAXI_IN'].max().sort_values(ascending = False)[:5]))

def ques6(cleanData):
    # function to calculate and print the relative percentages of flight time in terms of taxi out time, actual flying time, and taxi in time
    totElapTime = cleanData['ACTUAL_ELAPSED_TIME'].sum()
    totTaxiOut = cleanData['TAXI_OUT'].sum()
    totTaxiIn = cleanData['TAXI_IN'].sum()
    totAirTime = cleanData['AIR_TIME'].sum()
    print('\nRelative percentage of flight time in terms of taxi out time:\n', totTaxiOut/totElapTime * 100)
    print('\nRelative percentage of flight time in terms of actual flying time:\n', totAirTime/totElapTime * 100)
    print('\nRelative percentage of flight time in terms of taxi in time:\n', totTaxiIn/totElapTime * 100)

def ques7(cleanData):
    # function to calculate and print the top 5 airlines in terms of actual flight speed
    cleanData['SPEED'] = cleanData['DISTANCE']/(cleanData['AIR_TIME']/60)
    print('\nTop 5 airlines in terms of actual flight speed (in mph):')
    print(cleanData.groupby('CARRIER')['SPEED'].mean().sort_values(ascending = False)[:5])

def ques8(cleanData):
    # function to find out and print do flights that depart late fly faster than those that do not
    cleanData['ROUTE'] = cleanData['ORIGIN'] + '-' + cleanData['DEST']
    cleanData['SPEED'] = cleanData['DISTANCE']/(cleanData['AIR_TIME']/60)
    flDepLate = cleanData[cleanData['DEP_DELAY'] > 0]
    flDepOt = cleanData[cleanData['DEP_DELAY'] <= 0]
    flLateGb = flDepLate.groupby('ROUTE')['SPEED'].mean().reset_index()
    flOtGb = flDepOt.groupby('ROUTE')['SPEED'].mean().reset_index()
    flMerge = flLateGb.merge(flOtGb, how = 'inner', on = 'ROUTE')
    avgLate = flMerge['SPEED_x'].mean()
    avgOt = flMerge['SPEED_y'].mean()
    print('\nAverage speed of flights that depart late on same routes:\n', avgLate)
    print('\nAverage speed of flights that depart on time on same routes:\n', avgOt)
    if avgLate > avgOt:
        print('Yes, the flights that depart late fly faster than those that do not.\n')
    elif avgLate <= avgOt:
        print('No, the flights that depart late do not fly faster than those that do not.\n')

def ques9(cleanData):
    # function to visualize do longer flights arrive late more often than shorter flights
    cleanData['DISTANCE_GROUP'] = (cleanData['DISTANCE']/500).astype(int)*500+500
    cleanData = cleanData.sort_values(by = 'DISTANCE_GROUP')
    flCount = cleanData.groupby('DISTANCE_GROUP').size()
    flArrLate = cleanData[cleanData['ARR_DELAY'] > 0]
    flArrLateCount = flArrLate.groupby('DISTANCE_GROUP').size()
    flArrLatePer = flArrLateCount/flCount * 100
    distanceGroup = cleanData['DISTANCE_GROUP'].unique()
    df = pd.DataFrame(flArrLatePer, distanceGroup)
    ax = df.plot.bar(color = 'red', title = 'Bar graph of percentage arrival lateness vs flight length')
    ax.set(xlabel = 'Distance groups (in miles), eg. 500 = between 0 and 500, 1000 = between 500 and 1000, and so on', ylabel = 'Percentage arrival lateness %')
    df = df.reset_index()
    df.columns = ['DISTANCE_GROUP', 'PER_ARR_LATE']
    print(df)
    plt.show()

def ques10(cleanData):
    # function to find out and print which flights (morning, afternoon, evening), have a greater on time departure percentage and on time arrival percentage
    depMorn = cleanData.query('0 <= CRS_DEP_TIME < 1200')
    depNoon = cleanData.query('1200 <= CRS_DEP_TIME < 1800')
    depEven = cleanData.query('1800 <= CRS_DEP_TIME <= 2359')
    arrMorn = cleanData.query('0 <= CRS_ARR_TIME < 1200')
    arrNoon = cleanData.query('1200 <= CRS_ARR_TIME < 1800')
    arrEven = cleanData.query('1800 <= CRS_ARR_TIME <= 2359')
    otDepMornCount = len(depMorn[depMorn['DEP_DELAY'] <= 0])
    otDepMornPer = otDepMornCount/len(depMorn)*100
    otDepNoonCount = len(depNoon[depNoon['DEP_DELAY'] <= 0])
    otDepNoonPer = otDepNoonCount/len(depNoon)*100
    otDepEvenCount = len(depEven[depEven['DEP_DELAY'] <= 0])
    otDepEvenPer = otDepEvenCount/len(depEven)*100
    print('\nOn time departure percentage for morning flights:\n', otDepMornPer)
    print('\nOn time departure percentage for noon flights:\n', otDepNoonPer)
    print('\nOn time departure percentage for evening flights:\n', otDepEvenPer)
    if otDepMornPer > otDepEvenPer and otDepMornPer > otDepNoonPer:
        print('\nMorning flights have a greater on time departure percentage.\n')
    elif otDepNoonPer > otDepEvenPer and otDepNoonPer > otDepMornPer:
        print('\nMorning flights have a greater on time departure percentage.\n')
    elif otDepEvenPer > otDepNoonPer and otDepEvenPer > otDepMornPer:
        print('\nMorning flights have a greater on time departure percentage.\n')
    elif otDepMornPer == otDepNoonPer and otDepMornPer > otDepEvenPer and otDepNoonPer > otDepEvenPer:
        print('\nMorning and noon flights have equal and greater on time departure percentage.\n')
    elif otDepNoonPer == otDepEvenPer and otDepNoonPer > otDepMornPer and otDepEvenPer > otDepMornPer:
        print('\nNoon and evening flights have equal and greater on time departure percentage.\n')
    elif otDepMornPer == otDepEvenPer and otDepMornPer > otDepNoonPer and otDepEvenPer > otDepNoonPer:
        print('\nNoon and evening flights have equal and greater on time departure percentage.\n')
    else:
        print('\nMorning, noon and evening flights have equal on time departure percentage\n')

    otArrMornCount = len(arrMorn[arrMorn['ARR_DELAY'] <= 0])
    otArrMornPer = otArrMornCount/len(arrMorn)*100
    otArrNoonCount = len(arrNoon[arrNoon['ARR_DELAY'] <= 0])
    otArrNoonPer = otArrNoonCount/len(arrNoon)*100
    otArrEvenCount = len(arrEven[arrEven['ARR_DELAY'] <= 0])
    otArrEvenPer = otArrEvenCount/len(arrEven)*100
    print('\nOn time arrival percentage for morning flights:\n', otArrMornPer)
    print('\nOn time arrival percentage for noon flights:\n', otArrNoonPer)
    print('\nOn time arrival percentage for evening flights:\n', otArrEvenPer)
    if otArrMornPer > otArrEvenPer and otArrMornPer > otArrNoonPer:
        print('\nMorning flights have a greater on time arrival percentage.\n')
    elif otArrNoonPer > otArrEvenPer and otArrNoonPer > otArrMornPer:
        print('\nMorning flights have a greater on time arrival percentage.\n')
    elif otArrEvenPer > otArrNoonPer and otArrEvenPer > otArrMornPer:
        print('\nMorning flights have a greater on time arrival percentage.\n')
    elif otArrMornPer == otArrNoonPer and otArrMornPer > otArrEvenPer and otArrNoonPer > otArrEvenPer:
        print('\nMorning and noon flights have equal and greater on time arrival percentage.\n')
    elif otArrNoonPer == otArrEvenPer and otArrNoonPer > otArrMornPer and otArrEvenPer > otArrMornPer:
        print('\nNoon and evening flights have equal and greater on time arrival percentage.\n')
    elif otArrMornPer == otArrEvenPer and otArrMornPer > otArrNoonPer and otArrEvenPer > otArrNoonPer:
        print('\nNoon and evening flights have equal and greater on time arrival percentage.\n')
    else:
        print('\nMorning, noon and evening flights have equal on time departure percentage\n')

def ques11(cleanData):
    # function to find out and print which day in the month has a worse performance time based on departure lateness percentage - the holiday, the day before, or the day after
    majHol = '2017-07-04'
    dayBef = '2017-07-03'
    dayAft = '2017-07-05'
    majHolFl = cleanData[cleanData['FL_DATE'] == majHol]
    dayBefFl = cleanData[cleanData['FL_DATE'] == dayBef]
    dayAftFl = cleanData[cleanData['FL_DATE'] == dayAft]
    majHolDelFl = majHolFl[majHolFl['DEP_DELAY'] > 0]
    dayBefDelFl = dayBefFl[dayBefFl['DEP_DELAY'] > 0]
    dayAftDelFl = dayAftFl[dayAftFl['DEP_DELAY'] > 0]
    majHolFlDelPer = len(majHolDelFl)/len(majHolFl)*100
    dayBefFlDelPer = len(dayBefDelFl)/len(dayBefFl)*100
    dayAftFlDelPer = len(dayAftDelFl)/len(dayAftFl)*100
    print('\nDeparture lateness percentage on the major holiday:\n', majHolFlDelPer)
    print('\nDeparture lateness percentage on the day before major holiday:\n', dayBefFlDelPer)
    print('\nDeparture lateness percentage on the day after major holiday:\n', dayAftFlDelPer)
    if majHolFlDelPer > dayBefFlDelPer and majHolFlDelPer > dayAftFlDelPer:
        print('\nMajor holiday has a worse performance time based on departure lateness percentage.\n')
    elif dayBefFlDelPer > majHolFlDelPer and dayBefFlDelPer > dayAftFlDelPer:
        print('\nDay before major holiday has a worse performance time based on departure lateness percentage.\n')
    elif dayAftFlDelPer > majHolFlDelPer and dayAftFlDelPer > dayBefFlDelPer:
        print('\nDay after major holiday has a worse performance time based on departure lateness percentage.\n')
    elif majHolFlDelPer == dayBefFlDelPer and majHolFlDelPer > dayAftFlDelPer and dayBefFlDelPer > dayAftFlDelPer:
        print('\nMajor day and day before major holiday have equal and worse performance time based on departure lateness percentage.\n')
    elif dayAftFlDelPer == dayBefFlDelPer and dayAftFlDelPer > majHolFlDelPer and dayBefFlDelPer > majHolFlDelPer:
        print('\nDay before major holiday and day after major holiday have equal and worse performance time based on departure lateness percentage.\n')
    elif majHolFlDelPer == dayAftFlDelPer and majHolFlDelPer > dayBefFlDelPer and dayAftFlDelPer > dayBefFlDelPer:
        print('\nMajor holiday and day after major holiday have equal and worse performance time based on departure lateness percentage.\n')
    else:
        print('\nMajor holiday, day before major holiday and day after major holiday have equal performance time based on departure lateness percentage.\n')

def ques12(cleanData):
    # function to find out and print do flights on the weekend have a worse performance than those on weekdays in terms of arrival lateness percentage
    cleanData['DAY'] = pd.to_datetime(cleanData['FL_DATE']).dt.dayofweek # Monday = 0, Sunday = 6
    weekendFl = cleanData[(cleanData['DAY'] == 5) | (cleanData['DAY'] == 6)]
    weekdayFl = cleanData[(cleanData['DAY'] != 5) & (cleanData['DAY'] != 6)]
    lateArrWeekend = weekendFl[weekendFl['ARR_DELAY'] > 0]
    lateArrWeekday = weekdayFl[weekdayFl['ARR_DELAY'] > 0]
    lateArrWeekendPer = len(lateArrWeekend)/len(weekendFl) * 100
    lateArrWeekdayPer = len(lateArrWeekday)/len(weekdayFl) * 100
    print('\nArrival lateness percentage on weekend:\n', lateArrWeekendPer)
    print('\nArrival lateness percentage on weekdays:\n', lateArrWeekdayPer)
    if lateArrWeekendPer > lateArrWeekdayPer:
        print('\nYes, flights on the weekend have a worse performance than those on weekdays in terms of arrival lateness percentage.\n')
    elif lateArrWeekendPer < lateArrWeekdayPer:
        print('\nNo, flights on the weekend do not have a worse performance than those on weekdays in terms of arrival lateness percentage.\n')
    else:
        print('\nNo, flights on the weekend have a same performance as those on weekdays in terms of arrival lateness percentage.\n')

def ques13(cleanData):
    # function to calculate and print
    # 1. the top 5 airlines based on average departure lateness in Connecticut
    # 2. the top 5 airlines based on average arrival lateness in Connecticut
    # 3. the top 5 airports based on on time departure percentage in Northeast
    # 4. the top 5 airports based on on time arrival percentage in Northeast
    ctDepData = cleanData[cleanData['ORIGIN_STATE_ABR'] == 'CT']
    ctArrData = cleanData[cleanData['DEST_STATE_ABR'] == 'CT']
    ctDepLate = ctDepData[ctDepData['DEP_DELAY'] > 0]
    ctDepLateAvg = ctDepLate.groupby('CARRIER')['DEP_DELAY'].mean()
    print('\nTop 5 airlines based on average departure lateness in Connecticut:')
    print(ctDepLateAvg.sort_values(ascending = False)[:5])
    ctArrLate = ctArrData[ctArrData['ARR_DELAY'] > 0]
    ctArrLateAvg = ctArrLate.groupby('CARRIER')['ARR_DELAY'].mean()
    print('\nTop 5 airlines based on average arrival lateness in Connecticut:')
    print(ctArrLateAvg.sort_values(ascending = False)[:5])
    neStates = ['CT', 'ME', 'MA', 'NH', 'NJ', 'NY', 'PA', 'RI', 'VT', 'DE', 'MD']
    neDepData = cleanData[cleanData['ORIGIN_STATE_ABR'].isin(neStates)]
    neArrData = cleanData[cleanData['DEST_STATE_ABR'].isin(neStates)]
    neDepOt = neDepData[neDepData['DEP_DELAY'] <= 0]
    neDepCount = neDepData.groupby('ORIGIN').size()
    neDepOtCount = neDepOt.groupby('ORIGIN').size()
    neDepOtPer = neDepOtCount/neDepCount*100
    print('\nTop 5 best airports based on on time departure percentage in Northeast:')
    print(neDepOtPer.sort_values(ascending = False)[:5])
    neArrOt = neArrData[neArrData['ARR_DELAY'] <= 0]
    neArrCount = neArrData.groupby('DEST').size()
    neArrOtCount = neArrOt.groupby('DEST').size()
    neArrOtPer = neArrOtCount/neArrCount*100
    print('\nTop 5 best airports based on on time arrival percentage in Northeast:')
    print(neArrOtPer.sort_values(ascending = False)[:5])

def main():
    cleanData = ques0()
    while True:
        print('1. What are the top 5 airlines in terms of ontime departure percentage? ontime arrival percentage? average departure lateness? average arrival lateness?')
        print('2. What are the relative percentages of flights that leave and arrive on time vs leave on time and arrive late vs leave late and arrive on time, and leave and arrive late?')
        print('3. Do states in the northeast have worse time performance than the rest of the country based on average departure lateness?')
        print('4. What are the top 5 airports in terms of ontime departure percentage? ontime arrival percentage? average departure lateness? average arrival lateness?')
        print('5. For each of five major airports - LAX, JFK, DFW, ORD and ATL - what are the top 5 airlines in terms of the longest taxi out and taxi in times?')
        print('6. What are the relative percentages of flight time in terms of taxi out time, actual flying time, and taxi in time?')
        print('7. What are the top 5 airlines in terms of actual flight speed?')
        print('8. Do flights that depart late fly faster than those that do not? (compare flying times of the same routes when they are late and not)')
        print('9. Do longer flights arrive late more often than shorter flights? (plot percentage arrival lateness vs flight length)')
        print('10. Which flights (morning, afternoon, evening), have a greater on time departure percentage? on time arrival percentage?')
        print('11. Which day in the month has a worse performance time based on departure lateness percentage - the holiday, the day before, or the day after?')
        print('12. Do flights on the weekend have a worse performance than those on weekdays in terms of arrival lateness percentage?')
        print('13. What are top 5 airlines in Connecticut based on - average departure lateness, average arrival lateness? What are top 5 airports in the Northeast based on - ontime departure percentage, ontime arrival percentage?')
        print('Enter 0 to quit.')
        ques = input('Enter question number:\n')
        if ques == '1':
            ques1(cleanData)
        elif ques == '2':
            ques2(cleanData)
        elif ques == '3':
            ques3(cleanData)
        elif ques == '4':
            ques4(cleanData)
        elif ques == '5':
            ques5(cleanData)
        elif ques == '6':
            ques6(cleanData)
        elif ques == '7':
            ques7(cleanData)
        elif ques == '8':
            ques8(cleanData)
        elif ques == '9':
            ques9(cleanData)
        elif ques == '10':
            ques10(cleanData)
        elif ques == '11':
            ques11(cleanData)
        elif ques == '12':
            ques12(cleanData)
        elif ques == '13':
            ques13(cleanData)
        elif ques == '0':
            break
        else:
            print('Invalid input. Try again!')
    print('Thank you for using this program. Have a good time. Good bye!')

main()
