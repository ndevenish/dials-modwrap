project(fable)

add_library( fable INTERFACE )
target_include_directories(fable INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/.)

add_python_library ( fable_ext
            ext.cpp )

