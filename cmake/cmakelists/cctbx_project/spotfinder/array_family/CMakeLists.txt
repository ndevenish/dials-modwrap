add_python_library ( spotfinder_array_family_flex_ext
            flex_ext.cpp
            flex_distl_spot.cpp )
target_link_libraries(spotfinder_array_family_flex_ext spotfinder omptbx scitbx_boost_python)

