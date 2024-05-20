<?php
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_FILES['xmlfile'])) {
    $xmlfile = $_FILES['xmlfile']['tmp_name'];
    $xmlcontent = file_get_contents($xmlfile);

    libxml_disable_entity_loader(false);
    $dom = new DOMDocument();
    $dom->loadXML($xmlcontent, LIBXML_NOENT | LIBXML_DTDLOAD);  // XXE vulnerability

    $xml = simplexml_import_dom($dom);
    echo "<h1>XML Content</h1>";
    echo "<pre>" . htmlspecialchars($xml->asXML()) . "</pre>";
}
?>
<form method="POST" enctype="multipart/form-data" action="xxe.php">
    <input type="file" name="xmlfile">
    <input type="submit" value="Upload XML">
</form>
