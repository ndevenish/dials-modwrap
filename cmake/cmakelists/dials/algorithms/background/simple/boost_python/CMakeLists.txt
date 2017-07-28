add_python_library ( dials_algorithms_background_simple_ext
            background_simple_ext.cc
            creator.cc
            modeller.cc
            outlier_rejector.cc )
target_link_libraries(dials_algorithms_background_simple_ext cctbx scitbx_boost_python)

