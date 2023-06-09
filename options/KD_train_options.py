from .base_options import BaseOptions

class KDTrainOptions(BaseOptions):
    def initialize(self):
        BaseOptions.initialize(self)
        self.parser.add_argument('--display_freq', type=int, default=100, help='frequency of showing training results on screen')
        self.parser.add_argument('--display_single_pane_ncols', type=int, default=0, help='if positive, display all images in a single visdom web panel with certain number of images per row.')
        self.parser.add_argument('--update_html_freq', type=int, default=1000, help='frequency of saving training results to html')
        self.parser.add_argument('--print_freq', type=int, default=100, help='frequency of showing training results on console')
        self.parser.add_argument('--save_latest_freq', type=int, default=5000, help='frequency of saving the latest results')
        self.parser.add_argument('--save_epoch_freq', type=int, default=5, help='frequency of saving checkpoints at the end of epochs')
        self.parser.add_argument('--continue_train', action='store_true', help='continue training: load the latest model')
        self.parser.add_argument('--epoch_count', type=int, default=1, help='the starting epoch count, we save the model by <epoch_count>, <epoch_count>+<save_latest_freq>, ...')
        self.parser.add_argument('--phase', type=str, default='train', help='train, val, test, etc')
        self.parser.add_argument('--which_epoch', type=str, default='latest', help='which epoch to load? set to latest to use latest cached model')
        self.parser.add_argument('--niter', type=int, default=300, help='# of iter at starting learning rate')
        self.parser.add_argument('--niter_decay', type=int, default=0, help='# of iter to linearly decay learning rate to zero')
        self.parser.add_argument('--adambeta1', type=float, default=0.9, help='first momentum term of adam')
        self.parser.add_argument('--adambeta2', type=float, default=0.999, help='second momentum term of adam')
        self.parser.add_argument('--lr', type=float, default=0.0005, help='initial learning rate for adam')
        self.parser.add_argument('--pool_size', type=int, default=50, help='the size of image buffer that stores previously generated images')
        self.parser.add_argument('--use_html', action='store_true', help='save intermediate training results to [opt.checkpoints_dir]/[opt.name]/web/')
        self.parser.add_argument('--lr_policy', type=str, default='lambda', help='learning rate policy: lambda|step|plateau')
        self.parser.add_argument('--lr_decay_iters', type=int, default=50, help='multiply by a gamma every lr_decay_iters iterations')
        self.parser.add_argument('--init_weights', type=str, default='pretrained_models/places-googlenet.pickle', help='initiliaze network from, e.g., pretrained_models/places-googlenet.pickle')

        self.parser.add_argument('--sigma', type=float, default=100, help='Hyperparameter for Gt and CrossSimilarity loss proportion')
        self.parser.add_argument('--alpha', type=float, default=100, help='Hyperparameter for Gt and feature loss proportion')
        self.parser.add_argument('--T_path', type=str, help='Path of teacher network')
        self.parser.add_argument('--T_model', type=str, default='resnet50',
                                 help='chooses which model to use. [ resnet34 | resnet50 | resnet101 ]')

        self.parser.add_argument('-hintmodule', nargs='+', type=int, default=5,
                                 help='chooses which module feature maps to use as hint and guided. [ 1 | 2 | 3 | 4 | 5 | 6]')

        self.parser.add_argument('-SCmodule', nargs='+', type=int, default=3,
                                 help='chooses which module feature maps to use as CSloss. [ 1 | 2 | 3 | 4 | 5 | 6 ]')

        self.parser.add_argument('--KLSC', action='store_true',
                                 help='if true, Use KLloss at CScriterion')
        self.parser.add_argument('--pretrained', type=bool, default=True, help='Use ImageNet pretrained resnet')

        #self.parser.add_argument('--layerTrans', type=str, default='1x1',
        #                         help='chooses which model to use. [ 1x1 | fc | attention ]')

        self.isTrain = True
        self.isKD = True
