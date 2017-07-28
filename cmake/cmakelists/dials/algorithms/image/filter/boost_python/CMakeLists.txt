add_python_library ( dials_algorithms_image_filter_ext
            anisotropic_diffusion.cc
            convolve.cc
            distance.cc
            fano_filter.cc
            filter_ext.cc
            mean_and_variance.cc
            median.cc
            summed_area.cc )
target_link_libraries(dials_algorithms_image_filter_ext cctbx scitbx_boost_python)

