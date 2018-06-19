import matplotlib.pyplot as plt
import os

RESULT_DIRECTORY = "__results__/visualization"

def graph_scatter(result_analysis, showgraph=True):

    fig, subplots = plt.subplots(1, len(result_analysis), sharey=True)

    for index, result in enumerate(result_analysis):
        subplots[index].set_xlabel('{0}인 입국수'.format(result['country_name']))
        index == 0 and subplots[index].set_ylabel('외국인 입장객수')
        subplots[index].set_title('r = {:.5f}'.format(result['r']))
        subplots[index].scatter(result['x'], result['y'], edgecolor='none', alpha=0.75, s=6, c='black')

    # save file?
    save_filename = '%s/graph_scatter.png' % (RESULT_DIRECTORY)
    plt.savefig(save_filename, dpi=400, bbox_inches='tight')

    plt.subplots_adjust(wspace=0)

    # show graph?
    if showgraph:
        plt.show()

if os.path.exists(RESULT_DIRECTORY) is False:
    os.mkdir(RESULT_DIRECTORY)