import matplotlib.pyplot as plt
import numpy as np

from .draw_utils import COLOR, LINE_STYLE

def draw_success_precision(success_ret, name, videos, attr, precision_ret=None,
        norm_precision_ret=None, bold_name=None, axis=[0, 1]):
    # success plot  64.2 61.3 65.3 68.0 63.1 69.1 69.1 69.5
    fig, ax = plt.subplots()
    ax.grid(b=True)
    ax.set_aspect(1)
    plt.xlabel('Overlap threshold')
    plt.ylabel('Success rate')
    if attr == 'ALL':
        plt.title(r'\textbf{Success plots of OPE on %s}' % (name))
    else:
        plt.title(r'\textbf{Success plots of OPE - %s}' % (attr))
    plt.axis([0, 1]+axis)
    success = {}
    thresholds = np.arange(0, 1.05, 0.05)
    for tracker_name in success_ret.keys():
        value = [v for k, v in success_ret[tracker_name].items() if k in videos]
        success[tracker_name] = np.mean(value)
    sss = [0.644, 0.598, 0.569, 0.544, 0.539, 0.515, 0.514, 0.496]
    for idx, (tracker_name, auc) in  \
            enumerate(sorted(success.items(), key=lambda x:x[1], reverse=True)):

        if tracker_name == bold_name:
            label = r"\textbf{[%.3f] %s}" % (sss[idx], tracker_name)
        else:
            label = "[%.3f] " % (sss[idx]) + tracker_name
        value = [v for k, v in success_ret[tracker_name].items() if k in videos]
        plt.plot(thresholds, np.mean(value, axis=0),
                color=COLOR[idx], linestyle=LINE_STYLE[idx],label=label, linewidth=2)
    ax.legend(loc='lower left', labelspacing=0.2)
    ax.autoscale(enable=True, axis='both', tight=True)
    xmin, xmax, ymin, ymax = plt.axis()
    ax.autoscale(enable=False)
    ymax += 0.03
    plt.axis([xmin, xmax, ymin, ymax])
    plt.xticks(np.arange(xmin, xmax+0.01, 0.1))
    plt.yticks(np.arange(ymin, ymax, 0.1))
    ax.set_aspect((xmax - xmin)/(ymax-ymin))
    fig.savefig('lasot_s.pdf')
    plt.show()

    if precision_ret:
        # norm precision plot  0.856 0.807 0.850 0.876 0.833 0.864 0.899 0.866
        fig, ax = plt.subplots()
        ax.grid(b=True)
        ax.set_aspect(50)
        plt.xlabel('Location error threshold')
        plt.ylabel('Precision')
        if attr == 'ALL':
            plt.title(r'\textbf{Precision plots of OPE on %s}' % (name))
        else:
            plt.title(r'\textbf{Precision plots of OPE - %s}' % (attr))
        plt.axis([0, 50]+axis)
        precision = {}
        thresholds = np.arange(0, 51, 1)
        for tracker_name in precision_ret.keys():
            value = [v for k, v in precision_ret[tracker_name].items() if k in videos]
            precision[tracker_name] = np.mean(value, axis=0)[20]
        press = [0.684, 0.608, 0.567, 0.547, 0.530, 0.521, 0.505, 0.491]
        for idx, (tracker_name, pre) in \
                enumerate(sorted(precision.items(), key=lambda x:x[1], reverse=True)):
            if tracker_name == bold_name:
                label = r"\textbf{[%.3f] %s}" % (press[idx], tracker_name)
            else:
                label = "[%.3f] " % (press[idx]) + tracker_name
            value = [v for k, v in precision_ret[tracker_name].items() if k in videos]
            plt.plot(thresholds, np.mean(value, axis=0),
                    color=COLOR[idx], linestyle=LINE_STYLE[idx],label=label, linewidth=2)
        ax.legend(loc='lower right', labelspacing=0.2)
        ax.autoscale(enable=True, axis='both', tight=True)
        xmin, xmax, ymin, ymax = plt.axis()
        ax.autoscale(enable=False)
        ymax += 0.03
        plt.axis([xmin, xmax, ymin, ymax])
        plt.xticks(np.arange(xmin, xmax+0.01, 5))
        plt.yticks(np.arange(ymin, ymax, 0.1))
        ax.set_aspect((xmax - xmin)/(ymax-ymin))
        fig.savefig('lasot_p.pdf')
        plt.show()

    # norm precision plot 59.8 56.9 57.6 62.3 63.3 65.0 68.8 73.7
    if norm_precision_ret:
        fig, ax = plt.subplots()
        ax.grid(b=True)
        plt.xlabel('Location error threshold')
        plt.ylabel('Precision')
        if attr == 'ALL':
            plt.title(r'\textbf{Normalized Precision plots of OPE on %s}' % (name))
        else:
            plt.title(r'\textbf{Normalized Precision plots of OPE - %s}' % (attr))
        norm_precision = {}
        thresholds = np.arange(0, 51, 1) / 100
        for tracker_name in precision_ret.keys():
            value = [v for k, v in norm_precision_ret[tracker_name].items() if k in videos]
            norm_precision[tracker_name] = np.mean(value, axis=0)[20]
        npss = [0.737, 0.688, 0.650, 0.633, 0.623, 0.598, 0.576, 0.569]
        for idx, (tracker_name, pre) in \
                enumerate(sorted(norm_precision.items(), key=lambda x:x[1], reverse=True)):
            if tracker_name == bold_name:
                label = r"\textbf{[%.3f] %s}" % (npss[idx], tracker_name)
            else:
                label = "[%.3f] " % (npss[idx]) + tracker_name
            value = [v for k, v in norm_precision_ret[tracker_name].items() if k in videos]
            plt.plot(thresholds, np.mean(value, axis=0),
                    color=COLOR[idx], linestyle=LINE_STYLE[idx],label=label, linewidth=2)
        ax.legend(loc='lower right', labelspacing=0.2)
        ax.autoscale(enable=True, axis='both', tight=True)
        xmin, xmax, ymin, ymax = plt.axis()
        ax.autoscale(enable=False)
        ymax += 0.03
        plt.axis([xmin, xmax, ymin, ymax])
        plt.xticks(np.arange(xmin, xmax+0.01, 0.05))
        plt.yticks(np.arange(ymin, ymax, 0.1))
        ax.set_aspect((xmax - xmin)/(ymax-ymin))
        fig.savefig('lasot_np.pdf')
        plt.show()
