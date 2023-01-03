
charge_extra=0
police=0.44
base_charge=15.00

minutes=int(input("Enter the total of minutes used: "))
msg = int(input("Enter the total of messages used: "))

if minutes>50 and msg>50:
    charge_extra=0.25*(minutes-50)+0.15*(msg-50)
elif minutes>50 and not msg>50:
    charge_extra=0.25*(minutes-50)
elif minutes<=50 and msg>50:
    charge_extra =0.15*(50-msg)

sub_total=base_charge+police+charge_extra
taxes=0.05*sub_total
total=taxes+sub_total

print(f'The total minutes are:==>{minutes:10}\nThe extra minutes are==>{minutes-50:10}\nThe total msg are:==>{msg:10}\nThe extra msg are==>{msg-50 if msg>50 else msg:10}\ncharge extra is ==> {charge_extra:10}\npolice bill is ==> {police:10}\ntotal is ==> {total:10}')

print(charge_extra)
