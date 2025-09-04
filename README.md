# ROS 2 pointcloud <-> laserscan converters

This is a ROS 2 package that provides components to convert `sensor_msgs/msg/PointCloud2` messages to `sensor_msgs/msg/LaserScan` messages and back.
It is essentially a port of the original ROS 1 package.

## pointcloud\_to\_laserscan::PointCloudToLaserScanNode

This ROS 2 component projects `sensor_msgs/msg/PointCloud2` messages into `sensor_msgs/msg/LaserScan` messages.

### Published Topics

* `scan` (`sensor_msgs/msg/LaserScan`) - The output laser scan.

### Subscribed Topics

* `cloud_in` (`sensor_msgs/msg/PointCloud2`) - The input point cloud. No input will be processed if there isn't at least one subscriber to the `scan` topic.

### Parameters

* `min_height` (double, default: 2.2e-308) - The minimum height to sample in the point cloud in meters.
* `max_height` (double, default: 1.8e+308) - The maximum height to sample in the point cloud in meters.
* `angle_min` (double, default: -π) - The minimum scan angle in radians.
* `angle_max` (double, default: π) - The maximum scan angle in radians.
* `angle_increment` (double, default: π/180) - Resolution of laser scan in radians per ray.
* `queue_size` (double, default: detected number of cores) - Input point cloud queue size.
* `scan_time` (double, default: 1.0/30.0) - The scan rate in seconds. Only used to populate the scan_time field of the output laser scan message.
* `range_min` (double, default: 0.0) - The minimum ranges to return in meters.
* `range_max` (double, default: 1.8e+308) - The maximum ranges to return in meters.
* `target_frame` (str, default: none) - If provided, transform the pointcloud into this frame before converting to a laser scan. Otherwise, laser scan will be generated in the same frame as the input point cloud.
* `transform_tolerance` (double, default: 0.01) - Time tolerance for transform lookups. Only used if a `target_frame` is provided.
* `use_inf` (boolean, default: true) - If disabled, report infinite range (no obstacle) as range_max + 1. Otherwise report infinite range as +inf.

#### Bounding Box Filter Parameters

The following parameters control the bounding box filter, which can be used to filter out points inside a specified cubic region (e.g., robot body parts, sensor mounts):

* `use_bounding_box_filter` (boolean, default: false) - Enable or disable bounding box filtering.
* `bbox_min_x` (double, default: -1.0) - Minimum X coordinate of the bounding box in meters.
* `bbox_max_x` (double, default: 1.0) - Maximum X coordinate of the bounding box in meters.
* `bbox_min_y` (double, default: -1.0) - Minimum Y coordinate of the bounding box in meters.
* `bbox_max_y` (double, default: 1.0) - Maximum Y coordinate of the bounding box in meters.
* `bbox_min_z` (double, default: -1.0) - Minimum Z coordinate of the bounding box in meters.
* `bbox_max_z` (double, default: 1.0) - Maximum Z coordinate of the bounding box in meters.

## pointcloud\_to\_laserscan::LaserScanToPointCloudNode

This ROS 2 component re-publishes `sensor_msgs/msg/LaserScan` messages as `sensor_msgs/msg/PointCloud2` messages.

### Published Topics

* `cloud` (`sensor_msgs/msg/PointCloud2`) - The output point cloud.

### Subscribed Topics

* `scan_in` (`sensor_msgs/msg/LaserScan`) - The input laser scan. No input will be processed if there isn't at least one subscriber to the `cloud` topic.

### Parameters

* `queue_size` (double, default: detected number of cores) - Input laser scan queue size.
* `target_frame` (str, default: none) - If provided, transform the pointcloud into this frame before converting to a laser scan. Otherwise, laser scan will be generated in the same frame as the input point cloud.
* `transform_tolerance` (double, default: 0.01) - Time tolerance for transform lookups. Only used if a `target_frame` is provided.
