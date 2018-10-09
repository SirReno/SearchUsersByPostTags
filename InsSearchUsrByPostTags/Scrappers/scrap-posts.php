<?php
if($argc > 2)
{
    if ($argv[$argc-1]>0)
    {
        try
        {
            $list_of_files=fopen("list_of_files.txt", "w+")or die("unable to open file");
            for($arg=1; $arg<$argc-1; $arg++)
            {
                echo $arg;
                $file=fopen("hashtag_no_{$arg}.txt","w+")or die("unable to open file");
                require __DIR__ . '/../vendor/autoload.php';
                $instagram = \InstagramScraper\Instagram::withCredentials('<user_name>', '<user_password>', '<path/to/cache/folder_in_this_project>');
                $instagram->login();
                $no_tags=$argv[$argc-1];
                $medias = $instagram->getMediasByTag($argv[$arg], $no_tags);

                $i=0;
                for ($i = 0; $i < $no_tags; $i++) {
                    $textToWrite="{$medias[$i]->getShortCode()}\n";
                    fwrite($file, $textToWrite);
                }
                fclose($file);
                if($arg!=$argc-1)
                {
                    sleep(1);
                }

                fwrite($list_of_files, "hashtag_no_{$arg}.txt ");
            }
        } catch(Exception $e){
            echo 'Exception: ', $e->getMessage(), "\n";
        }
    }else{
        echo 'Not a valid number as second argument';
    }
}
