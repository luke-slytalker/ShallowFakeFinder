# ShallowFakeFinder
Python script I threw together that is basically the beginning for a proof of concept to help identify badly 'deep faked' videos.

The concept is that duplicate frames will exist in a deep fake video (granted, I'm sure this could be 'fixed' with a 2nd and 3rd pass algo to add slight lighting/brightness differences on a single, or set of, pixels).

The longer the video, I'd assume it would become more likely that a frame would have to be re-used (there's only so many permutations that can be used).

On it's own, the script isn't really able to discern one way or another; it's more of a tool to tailor to the analysis needed.  
A bounding box will be used to sample areas of the screen which will be hashed & compared.  In a background that's outdoors, there should be a number of lighting derivations and small movements of background objects caused by air currents or wind.  

TO ADD:
 - frequency analysis
 - bounding box
 - multiple bounding boxes
