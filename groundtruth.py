### groundtruth network #####
import sys
import lasagne_dependencies as vgg



def build_model():
	# load model with apply function
	network = vgg.build_model();
	network= vgg.load_model(network);
	# retrieve params
	vgg.get_params(network)
	vgg.get_filter_info(network)

def build_Fisher():
	raise NotImplementedError();


if __name__=="__main__":
	print 'kikou'
	build_model();
