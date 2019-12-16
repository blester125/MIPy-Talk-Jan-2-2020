def add_to_plot(ax, data, column, index=None, color=None):
    data = data.loc[(column,)]
    if index is not None:
        data = data.loc[data.index.isin(index)]
    x = data.index
    y = data[('time', 'mean')]
    yerr = data[('time', 'std')]
    ax.errorbar(x, y, yerr=yerr, label=column, c=color)
    return ax
