VALID_SIZE = 0.1

dataset = datasets.ImageFolder(TRAIN_PATH, train_transformations)
valid_len = int(len(dataset)*VALID_SIZE)
train_len = len(dataset) - valid_len

# разбиваем dataset на train_dataset и valid_dataset в заданном соотношение VALID_SIZE
train_dataset, valid_dataset = torch.utils.data.random_split(
    dataset,
    [train_len, valid_len],
    generator=torch.Generator().manual_seed(42)
)

valid_dataset.dataset.transform = test_transformations
[len(train_dataset), len(valid_dataset)]

# next_step

train_loader = torch.utils.data.DataLoader(
    train_dataset, 
    batch_size=BATCH_SIZE, 
    shuffle=True, # перемешать данные в случайном порядке
)

valid_loader = torch.utils.data.DataLoader(
    valid_dataset,
    batch_size=BATCH_SIZE,
    shuffle=False,
)

dataloaders_dict = {'train':  train_loader,
                    'val': valid_loader}

# test

for x, y in dataloaders_dict['train']:
  break
x.shape

import matplotlib.pyplot as plt

plt.imshow(x[1].permute(1, 2, 0))

def set_parameter_requires_grad(model, feature_extracting):
    if feature_extracting:
        for param in model.parameters():
            param.requires_grad = False
