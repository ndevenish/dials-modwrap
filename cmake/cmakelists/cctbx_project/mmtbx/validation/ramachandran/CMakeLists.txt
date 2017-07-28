add_python_library ( mmtbx_validation_ramachandran_ext
            rama_eval_bpl.cpp )
target_link_libraries(mmtbx_validation_ramachandran_ext cctbx scitbx_boost_python)

