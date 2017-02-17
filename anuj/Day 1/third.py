listm= ['jan','feb','march','april','may','june','july','aug','sep','oct','nov','dec']
value= raw_input("enter the quarter ")
value= int(value)
end= value*3
start= end-3
print listm[start:end]
