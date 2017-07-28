add_python_library ( scitbx_suffixtree_shared_ext
            suffixtree_shared_ext.cpp )
target_link_libraries(scitbx_suffixtree_shared_ext scitbx_boost_python)

add_python_library ( scitbx_suffixtree_single_ext
            suffixtree_single_ext.cpp
            object_extensions.cpp )
target_link_libraries(scitbx_suffixtree_single_ext scitbx_boost_python)

