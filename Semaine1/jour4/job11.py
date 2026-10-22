def time_to_text(minutes):
    heures = minutes // 60
    minutes_restantes = minutes % 60
    return f"{heures} heures et {minutes_restantes} minutes"

print(time_to_text(60))   
print(time_to_text(90))   
print(time_to_text(120))  
print(time_to_text(0))    
print(time_to_text(75))   