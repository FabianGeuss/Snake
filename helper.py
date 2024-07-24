from IPython import display
import matplotlib.pyplot as plt

plt.ion()

def plot(scores, mean_scores):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(mean_scores)
    plt.ylim(ymin=0)
    plt.text(len(scores)-1, mean_scores[-1], str(mean_scores[-1]))
