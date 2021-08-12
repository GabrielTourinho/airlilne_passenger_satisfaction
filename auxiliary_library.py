import numpy as np
import matplotlib.pyplot as plt


def plot_bar(
    xticklabels,
    rect_percentages,
    rects_labels,
    title,
):
    """Function that plots bar charts.

    Args:
        xticklabels (list): Labels for each of the x ticks.
        rect_percentages (list): List of the percentages which correspond to the
            bar height.
        rects_labels (list): List of the labels of the legend.
        title (str): Title of the bar plot.

    """

    x = np.arange(len(xticklabels))
    width = 0.35

    fig, ax = plt.subplots()

    if len(rect_percentages) == 2:
        rects1 = ax.bar(
            x - width / 2,
            rect_percentages[0],
            width,
            label=rects_labels[0],
        )
        rects2 = ax.bar(
            x + width / 2,
            rect_percentages[1],
            width,
            label=rects_labels[1],
        )

        ax.set_xticks(x)
    else:
        width = 0.25

        rects1 = ax.bar(
            x,
            rect_percentages[0],
            width,
            label=rects_labels[0],
        )
        rects1 = ax.bar(
            x + width,
            rect_percentages[1],
            width,
            label=rects_labels[1],
        )
        rects3 = ax.bar(
            x + 2 * width,
            rect_percentages[2],
            width,
            label=rects_labels[2],
        )

        ax.set_xticks(x + width)

    ax.set_ylabel("Rate")
    ax.set_title(title)
    ax.set_xticklabels(xticklabels)
    ax.set_yticks(np.arange(0, 1.1, 0.1))
    ax.legend()

    fig.tight_layout()

    plt.show()
