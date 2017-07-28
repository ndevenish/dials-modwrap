add_python_library ( mmtbx_scaling_ext
            scaling_ext.cpp
            twinning_bpl.cpp
            relative_scaling_bpl.cpp
            outlier_bpl.cpp )
target_link_libraries(mmtbx_scaling_ext cctbx scitbx_boost_python)

