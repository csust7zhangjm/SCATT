class EnvironmentSettings:
    def __init__(self):
        self.workspace_dir = ''    # Base directory for saving network checkpoints.
        self.tensorboard_dir = self.workspace_dir + '/tensorboard/'    # Directory for tensorboard files.
        self.lasot_dir = '/root/autodl-tmp/LaSOT/LaSOT/LaSOTBenchmark'
        self.got10k_dir = '/root/autodl-tmp/full_data/train_data/'
        self.trackingnet_dir = '/root/autodl-tmp/TrackingNet'
        self.coco_dir = '/root/autodl-tmp/COCO2017/'
        self.lvis_dir = ''
        self.sbd_dir = ''



        self.imagenet_dir = ''
        self.imagenetdet_dir = ''
        self.ecssd_dir = ''
        self.hkuis_dir = ''
        self.msra10k_dir = ''
        self.davis_dir = ''
        self.youtubevos_dir = ''
