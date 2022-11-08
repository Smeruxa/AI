# step - creating_model

model = models.resnet18(pretrained=True)

for param in model.parameters():
  param.requires_grad = False
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, NUM_CLASSES)

# step - check/set parametres

params_to_update = model.parameters()
print("Params to learn:")

params_to_update = []
for name,param in model.named_parameters():
    if param.requires_grad == True:
        params_to_update.append(param)
        print("\t",name)

model = model.to(DEVICE)

# step - train model

criterion = nn.CrossEntropyLoss().to(DEVICE)
optimizer = optim.Adagrad(params_to_update, lr=LR)
model = train_model(model, dataloaders_dict, criterion, optimizer, num_epochs=NUM_EPOCHS)
