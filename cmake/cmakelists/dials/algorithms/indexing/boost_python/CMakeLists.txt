add_python_library ( dials_algorithms_indexing_ext
            fft3d.cc
            indexing_ext.cc )
target_link_libraries(dials_algorithms_indexing_ext cctbx ann scitbx_boost_python)

