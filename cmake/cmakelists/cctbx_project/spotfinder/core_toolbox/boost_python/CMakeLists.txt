add_python_library ( spotfinder_hough_ext
            hough_ext.cpp )
target_link_libraries(spotfinder_hough_ext spotfinder omptbx scitbx_boost_python)

