import matplotlib.pyplot as plt

def generate_bar_chart(labels, value):
    fig, ax = plt.subplots()
    ax.bar(labels, value)
    plt.show()

if __name__ == '__main__':
    generate_bar_chart(['a','b','c'], [1,2,3])
