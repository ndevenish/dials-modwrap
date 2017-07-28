project(xfel)

add_library( xfel INTERFACE )
target_include_directories(xfel INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/..)

add_python_library ( acqiris_ext
            acqiris_ext.cpp )
target_link_libraries(acqiris_ext cctbx scitbx_boost_python)

add_python_library ( xfel_ext
            ext.cpp )
target_link_libraries(xfel_ext cctbx scitbx_boost_python)

add_python_library ( xfel_metrology_ext
            metrology_ext.cpp )
target_link_libraries(xfel_metrology_ext cctbx scitbx_boost_python)

add_subdirectory(metrology)
add_subdirectory(mono_simulation)
add_subdirectory(vonHamos)
