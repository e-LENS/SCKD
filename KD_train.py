import time
from options.KD_train_options import KDTrainOptions
from data.data_loader import CreateDataLoader
from models.models import create_model
from util.visualizer import Visualizer
import copy
import util.util as util
from PIL import Image

opt = KDTrainOptions().parse()
import torch
import numpy as np
import random

torch.manual_seed(opt.seed)
np.random.seed(opt.seed)
random.seed(opt.seed)
torch.backends.cudnn.deterministic = True

# Set Dataloader
data_loader = CreateDataLoader(opt)
dataset = data_loader.load_data()
dataset_size = len(data_loader)
print('#training images = %d' % dataset_size)

visualizer = Visualizer(opt)
total_steps = 0

# Set Student Model
student = create_model(opt)

## KD-Student Training
for epoch in range(opt.epoch_count, opt.niter + opt.niter_decay + 1):
    epoch_start_time = time.time()
    epoch_iter = 0

    for i, data in enumerate(dataset):
        iter_start_time = time.time()
        visualizer.reset()
        total_steps += opt.batchSize
        epoch_iter += opt.batchSize

        student.set_input(data)
        student.optimize_parameters()

        if total_steps % opt.print_freq == 0:
            errors = student.get_current_errors()
            t = (time.time() - iter_start_time) / opt.batchSize
            visualizer.print_current_errors(epoch, epoch_iter, errors, t)

            losses = student.get_current_errors()

            if opt.display_id > 0:
                visualizer.plot_current_errors(epoch, float(epoch_iter) / dataset_size, opt, errors)

    if epoch % opt.save_epoch_freq == 0:
        print('saving the model at the end of epoch %d, iters %d' %
              (epoch, total_steps))
        student.save('latest')
        student.save(epoch)

    print('End of epoch %d / %d \t Time Taken: %d sec' %
          (epoch, opt.niter + opt.niter_decay, time.time() - epoch_start_time))
    student.update_learning_rate()
