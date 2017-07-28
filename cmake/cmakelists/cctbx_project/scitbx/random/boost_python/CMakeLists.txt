add_python_library ( scitbx_random_ext
            random_ext.cpp
            basic_distributions.cpp )
target_link_libraries(scitbx_random_ext scitbx_boost_python)

