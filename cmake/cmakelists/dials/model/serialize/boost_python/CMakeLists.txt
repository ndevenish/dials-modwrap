add_python_library ( dials_model_serialize_ext
            serialize_ext.cc )
target_link_libraries(dials_model_serialize_ext cctbx scitbx_boost_python)

