import matplotlib.pyplot as plt

majors = ['Small', 'Medium', 'Large']  # TO DO
frequencies = [0.0625, 0.125, 0.1875, 0.25, 0.1875, 0.125, 0.0625]  # TO DO

bar_graph = plt.figure('Bar Graph')
plt.bar(majors, frequencies, edgecolor='black')
plt.title('Bar Graph')
bar_graph.savefig('bar_graph.png', format='png', dpi=1200)

pie_chart = plt.figure('Pie Chart')
plt.pie(frequencies, labels=majors, autopct='%1.0f%%')
plt.title('Pie Chart')
pie_chart.savefig('pie_chart.png', format='png', dpi=1200)

plt.show()

print('\n>>> END <<<')
