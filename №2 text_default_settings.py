NUM_CLASSES = 2
BATCH_SIZE = 128
NUM_EPOCHS = 50
DEVICE = 'cuda'
LR = 0.001

TRAIN_PATH = '/content/human detection dataset/'
TEST_PATH = '/content/human detection dataset/'

train_transformations  = torchvision.transforms.Compose(
    [
        torchvision.transforms.Resize((224, 224)),
        torchvision.transforms.RandomHorizontalFlip(p=0.5),
        torchvision.transforms.RandomVerticalFlip(p=0.5),
        torchvision.transforms.RandomRotation(40),
        torchvision.transforms.GaussianBlur(kernel_size=(1,7)),
        torchvision.transforms.RandomPosterize(bits=(10)),
        torchvision.transforms.ToTensor(),
        torchvision.transforms.Normalize(
            mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
        ),
    ]
)

test_transformations = transforms.Compose([
        torchvision.transforms.Resize(256),
        torchvision.transforms.CenterCrop(224),
        torchvision.transforms.ToTensor(),
        torchvision.transforms.Normalize(
            mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
        ),
])
