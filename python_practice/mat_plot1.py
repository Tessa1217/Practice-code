# matplot pyplot 
import matplotlib.pyplot as plt

plt.plot([10, 20, 30, 40, 50]) # Y
plt.show()

x = [1, 2, 3, 4, 5, 6, 7]
y = [12.5, 16, 28, 13.4, 19, 11.2, 17.3]
plt.plot(x, y)
plt.show()

# Weekly temp - Solid
import matplotlib.pyplot as plt
day = ["Mon", "Tue", "Weds", "Thurs", "Fri", "Sat", "Sun"]
max_temp = [6, 5, 7, 3, -1, 3, 6]
min_temp = [-4, -7, -5, -6, -9, -6, -9]
plt.plot(day, max_temp, label = "Max Temp")
plt.plot(day, min_temp, label = "Min Temp")
plt.xlabel("day")
plt.ylabel("temp")
plt.legend(loc = "upper left")
plt.title("Weekly Temperature")
plt.show()

# Weekly temp - Dot
import matplotlib.pyplot as plt
day = ["Mon", "Tue", "Weds", "Thurs", "Fri", "Sat", "Sun"]
max_temp = [6, 5, 7, 3, -1, 3, 6]
min_temp = [-4, -7, -5, -6, -9, -6, -9]
plt.plot(day, max_temp, "sb", label = "Max Temp")
plt.plot(day, min_temp, "sm", label = "Min Temp")
plt.xlabel("day")
plt.ylabel("temp")
plt.legend(loc = "upper left")
plt.title("Weekly Temperature")
plt.show()

# Weekly temp - Bar
import matplotlib.pyplot as plt
day = ["Mon", "Tue", "Weds", "Thurs", "Fri", "Sat", "Sun"]
max_temp = [6, 5, 7, 3, -1, 3, 6]
min_temp = [-4, -7, -5, -6, -9, -6, -9]
plt.bar(day, max_temp, label = "Max Temp")
plt.bar(day, min_temp, label = "Min Temp")
plt.xlabel("day")
plt.ylabel("temp")
plt.legend(loc = "upper left")
plt.title("Weekly Temperature")
plt.show()

