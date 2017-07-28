project(ccp4io_adaptbx)

add_library( ccp4io_adaptbx INTERFACE )
target_include_directories(ccp4io_adaptbx INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/..)

add_python_library ( ccp4io_adaptbx_ext
            ext.cpp )
target_link_libraries(ccp4io_adaptbx_ext ccp4io)

