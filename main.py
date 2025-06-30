import torchvision
import matplotlib.pyplot as plt

# Load the MNIST dataset
train_dataset = torchvision.datasets.MNIST(root='./data', train=True, download=True)
print(f"Number of training samples: {len(train_dataset)}")
for i in range(100):
    # print(train_dataset[i])  
    image, label = train_dataset[i]  # Get the first image
    if label == 8:  # Check if the label is 0
        print(f"Image shape: {image}, Label: {label}")
        plt.imsave('mnist_image.png', image, cmap='gray')
        

# plt.imshow("mnist_image.pnt", cmap='gray')

# Save the image as a PNG file
