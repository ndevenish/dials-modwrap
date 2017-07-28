add_python_library ( cctbx_dmtbx_ext
            dmtbx_ext.cpp
            triplet_generator.cpp
            triplet_phase_relation.cpp )
target_link_libraries(cctbx_dmtbx_ext cctbx scitbx_boost_python)

