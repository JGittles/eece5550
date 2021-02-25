
(cl:in-package :asdf)

(defsystem "guide-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "april" :depends-on ("_package_april"))
    (:file "_package_april" :depends-on ("_package"))
  ))