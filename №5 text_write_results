-- arguments
path = "/content/raw-img"
test_dataset = datasets.ImageFolder(path, test_transformations)
test_dataloader = torch.utils.data.DataLoader(test_dataset, batch_size=1)
model.eval()

#-- numerate

a = {}
for i, l in enumerate(os.listdir(path)):
  a[l] = i
def convert_dir(string):
  return a[string]
  
#-- dirs and Y to labels

image_label = []
for dir in os.listdir(path):
  for filename in os.listdir(path + '/' + dir):
    image_label.append([path + '/' + dir + '/' + filename, str(convert_dir(dir))])

#-- def predict'a

def predict(model, path):
  T = test_transformations(Image.open(path).convert('RGB')).to(DEVICE) 
  probs = model(T.unsqueeze(0)) 
  return torch.argmax(probs).cpu().numpy()
  
#-- input answers

answers = []
for path, label in image_label:
  label_pred = predict(model, path)
  answers.append([path, label_pred])

f = open('submission.csv', 'w')
for answer in answers:
  f.write(str(answer[0]) + ',' + str(answer[1]) + '\n')
f.close()
